import { Component, ViewChild } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { RegistrationService } from '../registration.service';
import { MatTabGroup } from '@angular/material/tabs';
import { CookieService } from 'ngx-cookie-service';
import {TokenResponse, User} from '../models';
import { Router } from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  @ViewChild('tabGroup') tabGroup!: MatTabGroup;

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
    private cookieService: CookieService,
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
        error: (err) => this.onError(err)
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
        // // Redirect the user to the home page
        this.router.navigate(['/']);
      } else {
        // Handle the case where the login credentials are invalid
        console.error('Invalid credentials');
      }
    });
    
  }


  private onSuccess(user: User): void {
    window.alert(`Thanks for registering: ${user.displayName}`);
    this.register.reset();
    this.tabGroup.selectedIndex = 0;
  }

  private onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

  private setCookie() {
    this.cookieService.set('my_cookie', 'cookie_value');
  }

  private getCookie() {
    const cookieValue = this.cookieService.get('my_cookie');
    console.log(cookieValue);
  }

}
