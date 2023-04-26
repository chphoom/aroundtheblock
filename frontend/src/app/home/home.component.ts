import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, User } from '../models';
import { PostsService } from '../posts.service';
import { RegistrationService } from '../registration.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  public current$: Observable<Challenge>;
  public mePosts$: Observable<Post[]>;
  public weChallenges$: Observable<Challenge[]>; 
  public prev$!: Observable<Challenge>
  public user: User | undefined;
  public isLoggedin: Boolean | undefined;
  public saved: Boolean | undefined;
  countdown!: string;

  constructor(private challengeService: ChallengeService,
     private postService: PostsService,
     private registrationService: RegistrationService,
     protected snackBar: MatSnackBar) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.mePosts$ = this.postService.getMePosts()
    this.weChallenges$ = this.challengeService.getWeChallenges()
    this.challengeService.getWeChallenges().subscribe(
      challenges => {
        const prevIndex = challenges.length - 2;
        this.prev$ = this.getElementAtIndex(prevIndex);
      }
    );
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

  getElementAtIndex(index: number): Observable<Challenge> {
    return this.weChallenges$.pipe(map((array: Challenge[]) => array[index]))
  }

  save(c: Challenge) {
    this.registrationService.saveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === c.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge saved!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unsave(c: Challenge) {
    this.registrationService.unsaveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user = user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === c.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge unsaved.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }
}
