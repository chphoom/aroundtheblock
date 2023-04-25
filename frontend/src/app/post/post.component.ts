import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Route } from '@angular/router';
import { Post, PostsService } from '../posts.service';
import { Challenge, User } from '../models';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  public post: Post;
  public user: User | undefined;
  public challenge: Challenge | undefined;
  
  public static Route: Route = {
    path: 'post/:id',
    component: PostComponent,
    resolve: {
      post: (route: ActivatedRouteSnapshot) => {
        const id = parseInt(route.paramMap.get('id')!);
        return inject(PostsService).getPost(id); 
    }
    }
  }

  constructor(private route: ActivatedRoute, private registrationService: RegistrationService, private challengeService: ChallengeService) {
    let data = route.snapshot.data as { post: Post };
    this.post = data.post;
    registrationService.getUser(this.post.user_id).subscribe(user => this.user = user)
    challengeService.getChallenge(this.post.challenge).subscribe(challenge => this.challenge = challenge)
    console.log(this.post.challenge)
  }

  ngOnInit() {
    
  }
}
