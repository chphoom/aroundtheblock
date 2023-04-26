import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-other-prof',
  templateUrl: './other-prof.component.html',
  styleUrls: ['./other-prof.component.css']
})
export class OtherProfComponent {
  public email: string = ""
  public user$!: Observable<User>;
  public user!: User;
  
  constructor(private route: ActivatedRoute, private registration_service: RegistrationService, private router: Router){}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.email = params.get('email') || ""
      this.user$ = this.registration_service.getUser(this.email)
      this.user$.subscribe(
        (user: User) => this.user = user
      )
    });
  }
}
