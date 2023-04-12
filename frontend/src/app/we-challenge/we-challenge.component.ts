import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public challengeService: ChallengeService;

  constructor(challengeService: ChallengeService) {
    this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService
  }
}
