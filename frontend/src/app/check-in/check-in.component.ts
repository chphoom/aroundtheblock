import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { CheckinService, Checkin, CheckInRequest} from '../checkin.service';
import {User} from '../registration.service';

@Component({
  selector: 'app-check-in',
  templateUrl: './check-in.component.html',
  styleUrls: ['./check-in.component.css']
})
export class CheckInComponent {
  form = this.formBuilder.group({
    pid: '',
  });

  constructor(
    private checkinService: CheckinService,
    private formBuilder: FormBuilder,
  ) {}

  onSubmit(): void {
    let form = this.form.value;
    let pid = parseInt(form.pid ?? "");
    

    this.checkinService
      .checkIn(pid)
      .subscribe({
        next: (checkIn) => this.onSuccess(checkIn),
        error: (err) => this.onError(err)
      });
    
  }
  private onSuccess(checkIn: Checkin): void {
    let user: User = checkIn.user
    window.alert(`Thanks for checking in: ${user.first_name} ${user.last_name}`);
    this.form.reset();
  }

  private onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}
