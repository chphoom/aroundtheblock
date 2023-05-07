import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SearchService } from '../search.service';
import { Post, PostsService } from '../posts.service';
import { RegistrationService, User } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { ActivatedRoute } from '@angular/router';
import { Observable, map, shareReplay } from 'rxjs';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  public posts$ = this.post_serv.getAllPosts().pipe(
    map(posts => posts.filter(post => !post.private))
  );
  public users$ = this.registrationService.getUsers().pipe(
    map(users => users.filter(user => !user.private))
  );
  public challenges$ = this.ch_serv.getAllChallenges()
  public query: string = "";
  
  public _user: User | undefined

  constructor(private route: ActivatedRoute, private router: Router, private search: SearchService, public post_serv: PostsService, public registrationService: RegistrationService, private ch_serv: ChallengeService) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
       this.query = params.get('query') || ""
       this.posts$ = this.search.Posts(this.query).pipe(
        map(posts => posts.filter(post => !post.private))
      );
       this.users$ = this.search.Users(this.query).pipe(
        map(posts => posts.filter(post => !post.private))
      );
       this.challenges$ = this.search.Challenges(this.query)
    });
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
    console.log("here" + newValue)
    return newValue;
  }

}
