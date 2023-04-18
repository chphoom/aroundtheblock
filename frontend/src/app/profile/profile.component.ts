import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  private isLoggedin: Boolean | undefined;
  user: User = {} as User;


  ngOnInit() {
    console.log(this.registration_service.isAuthenticated$)
    this.registration_service.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }
  
  constructor(private registration_service: RegistrationService, private router: Router){

  }

  logOut() {
    this.registration_service.logout();
    this.router.navigate(['/']);
  }

}
