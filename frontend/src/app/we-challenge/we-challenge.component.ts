import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  public current$: Observable<Challenge>;
  public wePosts$ = this.postsService.getWePosts();
  public weChallenges$: Observable<Challenge[]>;

  constructor(private router: Router, private challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private shareService: ShareService) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.weChallenges$ = this.challengeService.getWeChallenges()
  }

  async onSubmit() {
    this.current$.subscribe(challenge => {
      this.shareService.setCurrentValue(challenge);
    });
    await this.router.navigate(['/upload']);
  }
}
