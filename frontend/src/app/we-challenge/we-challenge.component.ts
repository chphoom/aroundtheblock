import { Component } from '@angular/core';
import { Observable, map, shareReplay } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, PostsService } from '../posts.service';
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
  public saved: Boolean | undefined;
  countdown!: string;
  public spoilerText = 'Show Spoilers';
  public blur = true;

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
    this.current$.subscribe(current => {
      const end = new Date(current.end!).getTime();
      setInterval(() => {
        const now = new Date().getTime();
        const distance = end - now;
        const days = Math.floor(distance / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');;
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');;
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');;
        const seconds = Math.floor((distance % (1000 * 60)) / 1000).toString().padStart(2, '0');;
        this.countdown = days + ':' + hours + ':' + minutes + ':' + seconds;
      }, 1000);
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

  toggleSpoiler() {
    //this.spoilerText = 'Show Spoilers' ? 'Hide Spoilers' : 'Show Spoilers';
    if (this.spoilerText == 'Show Spoilers') {
      this.spoilerText = 'Hide Spoilers';
    }
    else {
      this.spoilerText = 'Show Spoilers';
    }

    this.blur = !this.blur;
  }

  private userCache: { [key: string]: Observable<string> } = {};

  getUsername(post: Post): Observable<string> {
    const cachedValue = this.userCache[post.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(post.user_id).pipe(
      map(user => user ? `${user.displayName}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache[post.user_id] = newValue;
    return newValue;
  }

  private userCache2: { [key: string]: Observable<string> } = {};

  getPfp(post: Post): Observable<string> {
    const cachedValue = this.userCache2[post.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(post.user_id).pipe(
      map(user => user ? `${user.pfp}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache2[post.user_id] = newValue;
    return newValue;
  }
}
