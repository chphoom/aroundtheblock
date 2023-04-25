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
  public selected!: Challenge;

  constructor(private challengeService: ChallengeService) {
    this.weChallenges$ = challengeService.getWeChallenges()
    this.weChallenges$.subscribe((challenges) => {
      this.selected = challenges[challenges.length - 1];
      this.selected.id = challenges.length
    });
  }

  onClick(challenge: Challenge, i: number) {
    this.selected = challenge
    this.weChallenges$.subscribe(challenges => {
      this.selected.id = challenges?.length - i;
    });
  }
}
