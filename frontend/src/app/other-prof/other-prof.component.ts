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
  public displayName: string = "";
  public user$!: Observable<User>;
  public user!: User;
  
  constructor(private route: ActivatedRoute, private registration_service: RegistrationService, private router: Router){}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.displayName = params.get('displayName') || ""
      this.user$ = this.registration_service.getUserN(this.displayName)
      this.user$.subscribe(
        (user: User) => this.user = user
      )
    });
  }
}
