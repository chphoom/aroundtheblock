import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';
import { RegistrationService, User } from '../registration.service';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public current: Challenge | undefined;
  public wePosts$ = this.postsService.getWePosts();
  public weChallenges$: Observable<Challenge[]>;
  public user$: Observable<User> | undefined;
  public user: User | undefined;

  constructor(private router: Router, private challengeService: ChallengeService, private registrationService: RegistrationService, private postsService: PostsService, private uploadService: UploadService, private shareService: ShareService) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.challengeService.getCurrentChallenge().subscribe((chall: Challenge) => {
      this.current = chall;
    });
    this.weChallenges$ = this.challengeService.getWeChallenges()
    this.user$ = this.registrationService.getUserInfo();
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
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
    }, (error) => {
      console.error(error);
    });  
    console.log("button clicked " + this.user!.email + " " + this.current!.id)
  }
}
