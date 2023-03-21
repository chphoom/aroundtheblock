import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  isLoggedin = this.registration_service.isLoggedIn();
  user: User = {} as User;

  ngOnInit() {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }
  
  constructor(private registration_service: RegistrationService){}

}
