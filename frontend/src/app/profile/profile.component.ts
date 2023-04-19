import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  private isLoggedin: Boolean | undefined;
  public user$: Observable<User> | undefined;
  
  constructor(private registration_service: RegistrationService, private router: Router){}

  ngOnInit() {
    // verify authentication
    this.registration_service.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    // get current user information
    this.user$ = this.registration_service.getUserInfo();
  }

  logOut() {
    this.registration_service.logout();
    this.router.navigate(['/']);
  }
}
