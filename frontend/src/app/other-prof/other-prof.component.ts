import { Component } from '@angular/core';
import { RegistrationService, User } from '../registration.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Post } from '../models';

@Component({
  selector: 'app-other-prof',
  templateUrl: './other-prof.component.html',
  styleUrls: ['./other-prof.component.css']
})
export class OtherProfComponent {
  public displayName: string = "";
  public user$!: Observable<User>;
  public user!: User;
  public currUser!: User;
  public publicPosts!: Post[];
  
  constructor(private route: ActivatedRoute, private registrationService: RegistrationService, private router: Router){}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.displayName = params.get('displayName') || ""
      this.user$ = this.registrationService.getUserN(this.displayName)
      this.user$.subscribe(
        (user: User) => {
          this.user = user;
          this.publicPosts = user.userPosts!.filter(post => !post.private);
        }
      )
    });
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.currUser = user;
      console.log(user);
    })
    /* if (this.user.private && (this.currUser.email != this.user.email)) {
      this.router.navigate(['/'])
    } */
  }
}
