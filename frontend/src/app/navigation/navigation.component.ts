import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public isLoggedin = this.registration_service.isLoggedIn();
  
  constructor(private registration_service: RegistrationService){
    
  }

  ngOnInit() {
    this.isLoggedin = this.registration_service.isLoggedIn();
  }
}
