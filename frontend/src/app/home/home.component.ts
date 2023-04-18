import { Component } from '@angular/core';
import { Observable } from 'rxjs';
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

  constructor(challengeService: ChallengeService) {
    this.challenges$ = challengeService.getAllChallenges()
    this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService
  }
}