import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { Router } from '@angular/router';
import { Observable, map, shareReplay } from 'rxjs';
import { Challenge, Post } from '../models';
import { ShareService } from '../share.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  private isLoggedin: Boolean | undefined;
  public user: User | undefined;
  public saved: { [key: number]: boolean } = {};
  public privatePosts!: Post[];
  public publicPosts!: Post[];

  
  constructor(private registrationService: RegistrationService, private router: Router, private shareService: ShareService, protected snackBar: MatSnackBar){}

  ngOnInit() {
    // verify authentication
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    // get current user information
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
      user.savedChallenges?.forEach(challenge => {
        this.saved[challenge.id!] = !!user.savedChallenges?.find(chall => chall.id === challenge.id);
      });
      console.log(user);
      console.log(this.saved);
      this.privatePosts = this.user!.userPosts!.filter(post => post.private);
      this.publicPosts = this.user!.userPosts!.filter(post => !post.private);
    });
    for (let post in this.publicPosts) {
      console.log(post)
    }

  }

  async onSubmit(challenge: Challenge) {
    this.shareService.setCurrentValue(challenge)
    await this.router.navigate(['/upload']);
  }

  save(c: Challenge) {
    this.registrationService.saveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id)
      console.log(this.saved);
      this.snackBar.open(`Challenge saved!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unsave(c: Challenge) {
    this.registrationService.unsaveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user = user
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id);
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

  getType(challenge: Challenge){
    if(challenge.start){
      return "we"
    } else {
      return "me"
    }
  }

  private userCache: { [key: string]: Observable<string> } = {};

  getUsername(post: Post): Observable<string> {
    const cachedValue = this.userCache[post.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(post.user_id).pipe(
      map(user => user ? `${user.displayName}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache[post.user_id] = newValue;
    return newValue;
  }

  private userCache2: { [key: string]: Observable<string> } = {};

  getPfp(post: Post): Observable<string> {
    const cachedValue = this.userCache2[post.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(post.user_id).pipe(
      map(user => user ? `${user.pfp}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache2[post.user_id] = newValue;
    return newValue;
  }

}
