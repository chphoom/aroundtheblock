import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Challenge } from '../challenge.service';
import { Observable } from 'rxjs';

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
  public challenge$: Observable<Challenge> | undefined;
  // public fields: String[] | undefined;
  
  constructor(private registration_service: RegistrationService, private challengeService: ChallengeService, private formBuilder: FormBuilder){
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
      // Pass challenge and options to api
      this.challenge$ = this.challengeService.createChallenge(challenge, this.options)
      // Calling subscribe on this creates a new challenge fsr
      // this.challenge$.subscribe(val => console.log(val))
      this.options = []
    } else {
      window.alert("You must choose at least one option.")
    }
    
    console.log(this.options)
  }
}
