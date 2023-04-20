import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Challenge } from '../challenge.service';
import { Router } from '@angular/router';
import { PostsService } from '../posts.service';

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
  
  constructor(private router: Router, private postsService: PostsService, private registration_service: RegistrationService, private challengeService: ChallengeService, private formBuilder: FormBuilder){
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

  onSubmit() {
    // get list of options
    for (var option in this.form.value) {
      // check if at least one option is checked
      if (this.form.value[option]) {
        this.valid = true;
      }
      this.options.push(this.form.value[option])
    }

    if (this.valid) {
      // Construct new challenge
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
      // Pass challenge and options to api and put returned challenge into variable
      this.challengeService.createChallenge(challenge, this.options).subscribe(challenge => this.challenge = challenge)
      // this.colorBox[0].style.backgroundColor = this.challenge!.colors[0]

      this.options = []
      //this.router.navigate(['/generated'])
    } else {
      window.alert("You must choose at least one option.")
    }
  }
}
