import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';

@Component({
  selector: 'app-me-challenge',
  templateUrl: './me-challenge.component.html',
  styleUrls: ['./me-challenge.component.css']
})
export class MeChallengeComponent {
  isLoggedin = this.registration_service.isLoggedIn();
  
  constructor(private registration_service: RegistrationService){}
}
