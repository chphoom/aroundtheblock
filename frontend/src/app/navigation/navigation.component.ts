import { Component, ElementRef, ViewChild } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { User } from '../registration.service';
import { Router } from '@angular/router';
import { NotificationService, Notification } from '../notification.service';
import { PostsService } from '../posts.service';
import { CommentService, Comment } from '../comment.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public notifs$!: Observable<Notification[]>
  public user: User | undefined;
  @ViewChild('search', { static: true }) search!: ElementRef;

  constructor(private router: Router,
     public registration_service: RegistrationService,
     public notificationService: NotificationService,
     private commentService: CommentService) {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
      this.notifs$ = this.notificationService.getToUser(user.email)
    });
  }

  onSearch() {
    const query = this.search.nativeElement.value;
    // For example, you could navigate to the search page and pass the search term as a query parameter
    this.router.navigate(['/search', query]);  }

  onClickN(notif: Notification) {
    if(notif.comment_id) {
      let post_id = 0
      this.commentService.get(notif.comment_id).subscribe(
        (comment: Comment) => {
          post_id = comment.post
        }
      )
      this.router.navigate(['/post', post_id]);
    } else if (notif.challenge_id) {
      this.router.navigate(['/we-challenge']);
    }
    else {
      // handle some error idk
    }
  }
}
