import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { RegistrationService, User } from '../registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {

  form = this.formBuilder.group({
    email: '',
    displayName: '',
    password: ''
  });

  constructor(
    private registrationService: RegistrationService,
    private formBuilder: FormBuilder,
  ) {}

  onSubmit(): void {
    let form = this.form.value;
    let email = form.email ?? "";
    let displayName = form.displayName ?? "";
    let password = form.password ?? "";

    this.registrationService
      .registerUser(email, displayName, password, "")
      .subscribe({
        next: (user) => this.onSuccess(user),
        error: (err) => this.onError(err)
      });
  }

  private onSuccess(user: User): void {
    window.alert(`Thanks for registering: ${user.displayName}`);
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