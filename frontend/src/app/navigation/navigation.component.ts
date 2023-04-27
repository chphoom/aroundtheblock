import { Component, ElementRef, ViewChild } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { User } from '../registration.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {

  public user: User | undefined;
  @ViewChild('search', { static: true }) search!: ElementRef;

  constructor(private router: Router, public registration_service: RegistrationService) {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
  }

  onSearch() {
    const query = this.search.nativeElement.value;
    // For example, you could navigate to the search page and pass the search term as a query parameter
    this.router.navigate(['/search', query]);  }
}
