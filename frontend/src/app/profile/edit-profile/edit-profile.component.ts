import { Component } from '@angular/core';
import { Observable, map } from 'rxjs';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';
import { RegistrationService, User } from '../../registration.service';
import { DateAdapter } from '@angular/material/core';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';

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
    console.log(form)
    this.registrationService.updateUser(this.user!.email, form.pronouns!, form.displayName!, form.private!, null, form.bio!, null)
  }
  
}
