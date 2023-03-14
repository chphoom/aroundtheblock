import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { RegistrationService, User } from '../registration.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  login = this.formBuilder.group({
    email: '',
    password: ''
  });

  register = this.formBuilder.group({
    email: '',
    username: '',
    password: '',
    confirm: ''
  });

  constructor(
    private registrationService: RegistrationService,
    private formBuilder: FormBuilder,
  ) {}

  registerSubmit(): void {
    let form = this.register.value;
    let email = form.email ?? "";
    let displayName = form.username ?? "";
    let password = form.password ?? "";
    let confirm = form.confirm ?? "";

    this.registrationService
      .registerUser(email, displayName, password, confirm)
      .subscribe({
        next: (user) => this.onSuccess(user),
        error: (err) => this.onError(err)
      });
  }

  private onSuccess(user: User): void {
    window.alert(`Thanks for registering: ${user.displayName}`);
    this.register.reset();
  }

  private onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

}
