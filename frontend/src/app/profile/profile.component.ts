import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Challenge } from '../models';
import { ShareService } from '../share.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  private isLoggedin: Boolean | undefined;
  public user$: Observable<User> | undefined;
  public user: User | undefined;
  
  constructor(private registration_service: RegistrationService, private router: Router, private shareService: ShareService){}

  ngOnInit() {
    // verify authentication
    this.registration_service.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    // get current user information
    this.user$ = this.registration_service.getUserInfo();
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }

  async onSubmit(challenge: Challenge) {
    this.shareService.setCurrentValue(challenge)
    await this.router.navigate(['/upload']);
  }

  logOut() {
    this.registration_service.logout();
    this.router.navigate(['/']);
  }

}
