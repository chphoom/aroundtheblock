import { Component } from '@angular/core';
import { RegistrationService } from './registration.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  isLoggedin = this.registration_service.isLoggedIn();
  
  constructor(private registration_service: RegistrationService){}
}
