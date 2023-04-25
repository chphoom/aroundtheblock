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
  countdown!: string;

  constructor(private router: Router, private challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private shareService: ShareService) {
    this.current$ = this.challengeService.getCurrentChallenge()
    this.weChallenges$ = this.challengeService.getWeChallenges()
    this.current$.subscribe(current => {
      const end = new Date(current.end!).getTime();
      setInterval(() => {
        const now = new Date().getTime();
        const distance = end - now;
        const days = Math.floor(distance / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');;
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');;
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');;
        const seconds = Math.floor((distance % (1000 * 60)) / 1000).toString().padStart(2, '0');;
        this.countdown = days + ':' + hours + ':' + minutes + ':' + seconds;
      }, 1000);
    });
  }

  async onSubmit() {
    this.current$.subscribe(challenge => {
      this.shareService.setCurrentValue(challenge);
    });
    await this.router.navigate(['/upload']);
  }
}
