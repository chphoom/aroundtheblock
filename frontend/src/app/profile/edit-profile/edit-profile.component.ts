import { Component } from '@angular/core';
import { Observable, map } from 'rxjs';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';
import { RegistrationService, User } from '../../registration.service';
import { DateAdapter } from '@angular/material/core';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { TokenResponse } from 'src/app/models';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.css']
})
export class EditProfileComponent {
  public user: User | undefined;
  private isLoggedin: Boolean | undefined;
  form = this.formBuilder.group({
      email: new FormControl({disabled: true}),
      displayName: new FormControl('', Validators.required),
      pronouns: new FormControl(''),
      bio: new FormControl(''),
      private: [false]
  })

  constructor(private router: Router, private formBuilder: FormBuilder, private registrationService: RegistrationService) {
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
  }

  onSave() {
    let form = this.form.value
    this.registrationService.updateUser(this.user!.email, form.pronouns!, form.displayName!, form.private!, null, form.bio!, null)
    .subscribe((user: User) => {
      console.log(user);
      // Update authToken in local storage
      this.registrationService
      .loginUser(user.email, user.password)
      .subscribe((response) => {
        const token = response as TokenResponse;
        if (token) {
          // Store the authentication token for future use
          localStorage.setItem('authToken', token.access_token);
          console.log(token)
          // Redirect the user to the home page
          window.location.reload();
          // window.location.href = "/";
          /* this.router.navigate(['/']); */
        } else {
          // Handle the case where the login credentials are invalid
          console.error('Invalid credentials');
        }
      })
    }, (error) => {
      console.error(error);
    });  }
  
}
