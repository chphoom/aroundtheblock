import { Component } from '@angular/core';
import { Observable, last } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  public weChallenges: Challenge[] | undefined;
  public current$: Observable<Challenge>;
  public challengeService: ChallengeService;
  public previous: Challenge | undefined;
  

  constructor(challengeService: ChallengeService) {
    challengeService.getWeChallenges().subscribe(challenges => this.weChallenges = challenges)
    this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService
    this.weChallenges?.pop
    this.previous = this.weChallenges?.at(-1)
  }
}