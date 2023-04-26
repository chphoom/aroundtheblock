import { Component } from '@angular/core';
import { Observable, map } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { PostsService } from '../posts.service';
import { UploadService } from '../upload.service';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';
import { RegistrationService, User } from '../registration.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public current: Challenge | undefined;
  public wePosts$ = this.postsService.getWePosts();
  public weChallenges$ = this.challengeService.getWeChallenges()
  public user: User | undefined;
  public isLoggedin: Boolean | undefined;
  public saved: Boolean | undefined

  constructor(private router: Router, private challengeService: ChallengeService, private registrationService: RegistrationService, private postsService: PostsService, private uploadService: UploadService, private shareService: ShareService, protected snackBar: MatSnackBar) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.challengeService.getCurrentChallenge().subscribe((chall: Challenge) => {
      this.current = chall;
    });
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === this.current?.id);
      console.log(user);
      console.log(this.saved);
    });
  }

  async onSubmit() {
    this.current$.subscribe(challenge => {
      this.shareService.setCurrentValue(challenge);
    });
    await this.router.navigate(['/upload']);
  }

  save() {
    this.registrationService.saveChallenge(this.user!.email, this.current!.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === this.current?.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge saved!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unsave() {
    // TODO: implement unsave
    this.registrationService.unsaveChallenge(this.user!.email, this.current!.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user = user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === this.current?.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge unsaved.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }
}
