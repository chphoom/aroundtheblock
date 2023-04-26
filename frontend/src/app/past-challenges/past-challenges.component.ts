import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { RegistrationService, User } from '../registration.service';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-past-challenges',
  templateUrl: './past-challenges.component.html',
  styleUrls: ['./past-challenges.component.css']
})
export class PastChallengesComponent {
  public weChallenges$!: Observable<Challenge[]>;
  public selected!: Challenge;
  public isLoggedin = this.registrationService.isLoggedIn();
  public user: User | undefined;

  constructor(private router: Router, private shareService: ShareService, private challengeService: ChallengeService, private registrationService: RegistrationService) {
    this.weChallenges$ = challengeService.getWeChallenges()
    this.weChallenges$.subscribe((challenges) => {
      this.selected = challenges[challenges.length - 1];
      this.selected.id = challenges.length
    });
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }

  onClick(challenge: Challenge, i: number) {
    this.selected = challenge
    this.weChallenges$.subscribe(challenges => {
      this.selected.id = challenges?.length - i;
    });
  }

  async onSubmit(){
    this.shareService.setCurrentValue(this.selected)
    await this.router.navigate(['/upload']);
  }
}
