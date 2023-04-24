import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Challenge, ChallengeService } from '../challenge.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  public challenges$: Observable<Challenge[]>;
  public current$: Observable<Challenge>;
  public challengeService: ChallengeService;
  public weChallenges$: Observable<Challenge[]>; 
  public prev$: Observable<Challenge>

  constructor(challengeService: ChallengeService) {
    console.log("home component")
    this.challenges$ = challengeService.getAllChallenges()
    this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService
    this.weChallenges$ = challengeService.getWeChallenges()
    this.prev$ = this.getElementAtIndex(this.weChallenges$.length - 2)
  }

  getElementAtIndex(index: number): Observable<Challenge> {
    return this.weChallenges$.pipe(map((array: Challenge[]) => array[index]))
  }
}