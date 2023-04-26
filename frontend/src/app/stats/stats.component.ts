import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { RegistrationService, User } from '../registration.service';
import { DeleteService } from '../delete.service';
import { Challenge } from '../models';
import { ChallengeService } from '../challenge.service';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.css']
})
export class StatsComponent {

  public users$: Observable<User[]>;
  public challenges$: Observable<Challenge[]>

  constructor(private registrationService: RegistrationService, 
    private deleteService: DeleteService,
    private challengeService: ChallengeService) {
    this.users$ = this.registrationService.getUsers()
    this.challenges$ = this.challengeService.getWeChallenges()
  }

  onSubmitU(user: User): void {
    this.deleteService.deleteUser(user).subscribe({
      next: (user) => this.onSuccessU(user),
      error: (err) => this.onError(err)
    });
    
  }

  onSubmitC(c: Challenge): void {
    this.deleteService.deleteChallenge(c).subscribe({
      next: (challenge) => this.onSuccessC(challenge),
      error: (err) => this.onError(err)
    })
  }

  private onSuccessU(user: User): void {
    //update users and checkings
    this.users$ = this.registrationService.getUsers()
    window.alert(`The deleted user is': ${user.displayName}`);
  }

  private onSuccessC(c: Challenge): void {
    //update users and checkings
    this.challenges$ = this.challengeService.getWeChallenges()
    window.alert(`The deleted challenge is': ${c.id}`);
  }

  private onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}