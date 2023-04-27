import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { SearchService } from '../search.service';
import { PostsService } from '../posts.service';
import { RegistrationService } from '../registration.service';
import { map } from 'rxjs';

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

  constructor(private route: ActivatedRoute, private router: Router, private search: SearchService, private post_serv: PostsService, private user_serv: RegistrationService) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
       this.query = params.get('query') || ""
       this.posts$ = this.search.Posts(this.query).pipe(
        map(posts => posts.filter(post => !post.private))
      );
    });
  }
}
