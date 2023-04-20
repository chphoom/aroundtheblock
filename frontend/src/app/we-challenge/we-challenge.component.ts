import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { PostsService } from '../posts.service';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public challengeService: ChallengeService;
  public wePosts$ = this.postsService.getWePosts();

  constructor(challengeService: ChallengeService, private postsService: PostsService) {
    this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService
    
  }
}
