import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Challenge } from '../models';
import { ShareService } from '../share.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  private isLoggedin: Boolean | undefined;
  public user$: Observable<User> | undefined;
  public user: User | undefined;
  public saved: Boolean | undefined;
  
  constructor(private registrationService: RegistrationService, private router: Router, private shareService: ShareService, protected snackBar: MatSnackBar){}

  ngOnInit() {
    // verify authentication
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    // get current user information
    this.user$ = this.registrationService.getUserInfo();
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }

  async onSubmit(challenge: Challenge) {
    this.shareService.setCurrentValue(challenge)
    await this.router.navigate(['/upload']);
  }

  save(id: number) {
    this.registrationService.saveChallenge(this.user!.email, id).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === id);
      console.log(this.saved);
      this.snackBar.open(`Challenge saved!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unsave(id: number) {
    this.registrationService.unsaveChallenge(this.user!.email, id).subscribe((user: User) => {
      console.log(user);
      this.user = user
      this.saved = !!user.savedChallenges?.find(challenge => challenge.id === id);
      console.log(this.saved);
      this.snackBar.open(`Challenge unsaved.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  logOut() {
    this.registrationService.logout();
    this.router.navigate(['/']);
  }

}
