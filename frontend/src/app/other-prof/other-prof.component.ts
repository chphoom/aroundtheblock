import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, map, shareReplay } from 'rxjs';
import { Post } from '../models';

@Component({
  selector: 'app-other-prof',
  templateUrl: './other-prof.component.html',
  styleUrls: ['./other-prof.component.css']
})
export class OtherProfComponent {
  public displayName: string = "";
  public user$!: Observable<User>;
  public user!: User;
  public currUser!: User;
  public publicPosts!: Post[];
  
  constructor(private route: ActivatedRoute, private registrationService: RegistrationService, private router: Router){}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.displayName = params.get('displayName') || ""
      this.user$ = this.registrationService.getUserN(this.displayName)
      this.user$.subscribe(
        (user: User) => {
          this.user = user;
          this.publicPosts = user.userPosts!.filter(post => !post.private);
        }
      )
    });
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.currUser = user;
      console.log(user);
    })
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
