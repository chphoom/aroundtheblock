import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post } from '../models';
import { PostsService } from '../posts.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  public current$: Observable<Challenge>;
  public mePosts$: Observable<Post[]>;
  public weChallenges$: Observable<Challenge[]>; 
  public prev$: Observable<Challenge>

  constructor(private challengeService: ChallengeService, private postService: PostsService) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.mePosts$ = this.postService.getMePosts()
    this.weChallenges$ = this.challengeService.getWeChallenges()
    this.prev$ = this.getElementAtIndex(this.weChallenges$.length - 2)
  }

  getElementAtIndex(index: number): Observable<Challenge> {
    return this.weChallenges$.pipe(map((array: Challenge[]) => array[index]))
  }
}