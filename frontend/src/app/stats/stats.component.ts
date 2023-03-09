import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { RegistrationService, User } from '../registration.service';
// import { CheckinService, Checkin } from '../checkin.service';
import { DeleteService } from '../delete.service';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.css']
})
export class StatsComponent {

  public users$: Observable<User[]>;

  constructor(private registrationService: RegistrationService, 
    private deleteService: DeleteService) {
    this.users$ = this.registrationService.getUsers()
  }

  onSubmit(user: User): void {
    this.deleteService.deleteUser(user).subscribe({
      next: (user) => this.onSuccess(user),
      error: (err) => this.onError(err)
    });
    
  }
  private onSuccess(user: User): void {
    //update users and checkings
    this.users$ = this.registrationService.getUsers()
    window.alert(`The deleted user is': ${user.displayName}`);
  }

  private onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}