import { Component, ViewChild } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { RegistrationService } from '../registration.service';
import { MatTabGroup } from '@angular/material/tabs';
import { TokenResponse, User } from '../models';
import { Router } from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  @ViewChild('tabGroup') tabGroup!: MatTabGroup;

  login = this.formBuilder.group({
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  });

  register = this.formBuilder.group({
    email: new FormControl('', Validators.required),
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
    confirm: new FormControl('', Validators.required)
  });

  public isLoggedin = this.registrationService.isLoggedIn();

  constructor(
    private registrationService: RegistrationService,
    private formBuilder: FormBuilder,
    private router: Router
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
        error: (err) => this.onRegisterError(err)
      });
  }

  loginSubmit(): void {
    let form = this.login.value;
    let email = form.email ?? "";
    let password = form.password ?? "";

    this.registrationService
    .loginUser(email, password)
    .subscribe((response) => {
      const token = response as TokenResponse;
      if (token) {
        // Store the authentication token for future use
        localStorage.setItem('authToken', token.access_token);
        console.log(token)
        // Redirect the user to the home page
        window.location.reload();
        window.location.href = "/";
      }
    }, (error) => this.onLoginError(error));
  }


  private onSuccess(user: User): void {
    window.alert(`Thanks for registering: ${user.displayName}`);
    this.register.reset();
    this.tabGroup.selectedIndex = 0;
  }

  private onRegisterError(err: Error) {
    if (err.message) {
      window.alert(`Registration failed. Please check fields again.`);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

  private onLoginError(err: Error) {
    if (err.message) {
      window.alert(`Login failed. Check email or password again.`);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

}
