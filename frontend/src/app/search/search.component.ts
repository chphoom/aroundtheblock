import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SearchService } from '../search.service';
import { PostsService } from '../posts.service';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { ActivatedRoute } from '@angular/router';
import { map } from 'rxjs';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  public posts$ = this.post_serv.getAllPosts().pipe(
    map(posts => posts.filter(post => !post.private))
  );
  public users$ = this.user_serv.getUsers().pipe(
    map(posts => posts.filter(post => !post.private))
  );
  public challenges$ = this.ch_serv.getAllChallenges()
  public query: string = ""

  constructor(private route: ActivatedRoute, private router: Router, private search: SearchService, private post_serv: PostsService, private user_serv: RegistrationService, private ch_serv: ChallengeService) {
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

}
