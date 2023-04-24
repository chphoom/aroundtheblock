import { Component } from '@angular/core';
import { Observable, last } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post } from '../models';
import { PostsService } from '../posts.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  public weChallenges: Challenge[] | undefined;
  public current$: Observable<Challenge>;
  public previous: Challenge | undefined;
  public mePosts$: Observable<Post[]>;

  constructor(private challengeService: ChallengeService, private postService: PostsService) {
    this.current$ = challengeService.getCurrentChallenge()
    this.mePosts$ = postService.getMePosts();
    // TODO: get previous challenge
  }
}