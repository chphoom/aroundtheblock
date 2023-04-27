import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { RegistrationService, User } from '../registration.service';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-past-challenges',
  templateUrl: './past-challenges.component.html',
  styleUrls: ['./past-challenges.component.css']
})
export class PastChallengesComponent {
  public weChallenges$!: Observable<Challenge[]>;
  public selected!: Challenge;
  public isLoggedin: Boolean | undefined;
  public user: User | undefined;
  public newID: number = 0;
  public saved: { [key: number]: boolean } = {};


  constructor(private router: Router,
     private shareService: ShareService,
      private challengeService: ChallengeService,
       private registrationService: RegistrationService,
       protected snackBar: MatSnackBar) {
    this.weChallenges$ = challengeService.getWeChallenges()
    this.weChallenges$.subscribe((challenges) => {
      this.selected = challenges[challenges.length - 1];
      this.newID = challenges.length
    });
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
      user.savedChallenges?.forEach(challenge => {
        this.saved[challenge.id!] = !!user.savedChallenges?.find(chall => chall.id === challenge.id);
      });
      console.log(user);
      console.log(this.saved);
    });
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
  }

  onClick(challenge: Challenge, i: number) {
    this.selected = challenge
    this.weChallenges$.subscribe(challenges => {
      this.newID = challenges?.length - i;
    });
  }

  async onSubmit(){
    this.shareService.setCurrentValue(this.selected)
    await this.router.navigate(['/upload']);
  }

  save(c: Challenge) {
    this.registrationService.saveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id)
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
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge unsaved.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }
}
