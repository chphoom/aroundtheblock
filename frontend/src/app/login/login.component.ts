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
    displayName: '',
    password: ''
  });

  constructor(
    private registrationService: RegistrationService,
    private formBuilder: FormBuilder,
  ) {}

}
