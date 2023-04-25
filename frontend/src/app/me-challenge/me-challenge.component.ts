import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Challenge } from '../challenge.service';
import { Router } from '@angular/router';
import { PostsService } from '../posts.service';
import { Observable } from 'rxjs';
import { ShareService } from '../share.service';
import {ThemePalette} from '@angular/material/core';
import {ProgressSpinnerMode} from '@angular/material/progress-spinner';
import { LoadingService } from '../loading.service';

@Component({
  selector: 'app-me-challenge',
  templateUrl: './me-challenge.component.html',
  styleUrls: ['./me-challenge.component.css']
})
export class MeChallengeComponent {
  public isLoggedin = this.registration_service.isLoggedIn();
  private options: String[];
  public form: FormGroup;
  private valid: Boolean = false;
  public challenge: Challenge | undefined;
  public colorBox = document.getElementsByClassName('color-box') as HTMLCollectionOf<HTMLElement>;
  public mePosts$ = this.postsService.getMePosts();
  public user: User | undefined;
  //public generator = "false";

  /* color: ThemePalette = 'primary';
  mode: ProgressSpinnerMode = 'indeterminate';
  value = 50; */
  
  constructor(private router: Router, private postsService: PostsService, private registration_service: RegistrationService, private challengeService: ChallengeService, private formBuilder: FormBuilder, private shareService: ShareService, protected loadingService: LoadingService){
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
    
    this.options = [];
    this.form = this.formBuilder.group({
      noun: [false],
      verb: [false],
      adj: [false],
      emotion: [false],
      style: [false],
      colors: [false]
    });
  }

  onGenerate() {
    //this.generator = "clicked"
    // get list of options
    for (var option in this.form.value) {
      // check if at least one option is checked
      if (this.form.value[option]) {
        this.valid = true;
      }
      this.options.push(this.form.value[option])
    }

    if (this.valid) {
      // Check if user is logged in and creates a challenge with user as author
      const challenge: Challenge = {
        id: 0,
        posts: [],
        noun: "", 
        verb: "", 
        adj: "", 
        emotion: "", 
        style: "", 
        colors: [],
        start: null,
        end: null,
        createdBy: null
      }
      if (this.user) {
        challenge.createdBy = this.user.email
      }

      // Construct new challenge
      // Pass challenge and options to api and put returned challenge into variable
      this.challengeService.createChallenge(challenge, this.options).subscribe(challenge => this.challenge = challenge)
      // keep this console log to keep track of created challenges
      console.log(this.challenge)
    } else {
      window.alert("You must choose at least one option.")
    }
    //this.generator = "success";
    this.options = [];
  }

  async onSubmit() {
    this.shareService.setCurrentValue(this.challenge)
    await this.router.navigate(['/upload']);
  }
}
