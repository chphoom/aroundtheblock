import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';
import { RegistrationService, User } from '../registration.service';
import { TokenResponse } from '../models';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public current: Challenge | undefined;
  public wePosts$ = this.postsService.getWePosts();
  public weChallenges$: Observable<Challenge[]>;
  public user$: Observable<User> | undefined;
  public user: User | undefined;
  public isLoggedin: Boolean | undefined;

  constructor(private router: Router, private challengeService: ChallengeService, private registrationService: RegistrationService, private postsService: PostsService, private uploadService: UploadService, private shareService: ShareService) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.challengeService.getCurrentChallenge().subscribe((chall: Challenge) => {
      this.current = chall;
    });
    this.weChallenges$ = this.challengeService.getWeChallenges()
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    this.user$ = this.registrationService.getUserInfo();
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }

  async onSubmit() {
    this.current$.subscribe(challenge => {
      this.shareService.setCurrentValue(challenge);
    });
    await this.router.navigate(['/upload']);
  }

  save() {
    this.registrationService.saveChallenge(this.user!.email, this.current!.id ?? 1).subscribe((user: User) => {
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
          // window.location.href = "/";
          /* this.router.navigate(['/']); */
        } else {
          // Handle the case where the login credentials are invalid
          console.error('Invalid credentials');
        }
      })
    }, (error) => {
      console.error(error);
    });


    this.user$ = this.registrationService.getUserInfo();
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });

    // change icon upon saving
    /* const icon = document.getElementById('save-icon');
    icon!.innerHTML = '<path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4z"/><path d="M4.268 1A2 2 0 0 1 6 0h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L13 13.768V2a1 1 0 0 0-1-1H4.268z"/>'; */
  }

  unsave() {
    // TODO: implement unsave
    this.registrationService.unsaveChallenge(this.user!.email, this.current!.id ?? 1).subscribe((user: User) => {
      console.log(user);
    }, (error) => {
      console.error(error);
    });
  }
}
