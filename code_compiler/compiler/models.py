from django.db import models

class PlayerProgress(models.Model):
    player_id = models.CharField(max_length=100, unique=True)  # Store player identifier (e.g., from Unity)
    unlocked_levels = models.IntegerField(default=1)  # Start with level 1

    def __str__(self):
        return f"Player {self.player_id}: Level {self.unlocked_levels}"