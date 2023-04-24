import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { User } from '../registration.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {

  public user: User | undefined;

  constructor(public registration_service: RegistrationService) {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }
}
