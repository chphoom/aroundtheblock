import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { SearchService } from '../search.service';
import { Post, PostsService } from '../posts.service';
import { RegistrationService } from '../registration.service';
import { Observable, map, shareReplay } from 'rxjs';

@Component({
  selector: 'app-tagged-posts',
  templateUrl: './tagged-posts.component.html',
  styleUrls: ['./tagged-posts.component.css']
})
export class TaggedPostsComponent {
  public posts$ = this.post_serv.getAllPosts().pipe(
    map(posts => posts.filter(post => !post.private))
  );
 
  public query: string = "";

  constructor(private route: ActivatedRoute, private router: Router, private search: SearchService, private post_serv: PostsService, private registrationService: RegistrationService) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
       this.query = params.get('query') || ""
       this.posts$ = this.search.Posts(this.query).pipe(
        map(posts => posts.filter(post => !post.private))
      );
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
