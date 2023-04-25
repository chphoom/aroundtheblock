import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';

@Component({
  selector: 'app-past-challenges',
  templateUrl: './past-challenges.component.html',
  styleUrls: ['./past-challenges.component.css']
})
export class PastChallengesComponent {
  public weChallenges$!: Observable<Challenge[]>;

  constructor(private challengeService: ChallengeService) {
    this.weChallenges$ = challengeService.getWeChallenges()
  }
}
