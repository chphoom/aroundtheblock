import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-me-challenge',
  templateUrl: './me-challenge.component.html',
  styleUrls: ['./me-challenge.component.css']
})
export class MeChallengeComponent {
  isLoggedin = this.registration_service.isLoggedIn();
  private options: String[];
  public form: FormGroup;
  
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
    for (var option in this.form.value) {
      this.options.push(this.form.value[option])
    }
    this.challengeService.createChallenge(this.options)
    // console.log(this.options)
  }
}
