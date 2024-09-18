# How should we teach brain imaging?

I've been teaching brain imaging for almost as long as I've been using
brain imaging - which - I just calculated - is now almost 30 years.
This talk is about how some colleagues and I ended up changing from
the well-established slides-and-workshop method to a radically
different approach, that has been called "code-first" or
"code-to-learn".  The approach combines teaching of the ideas with
teaching for organized and reproducible analysis.   We wrote up the
motivation, design and experience of these courses in [^1].

My journey started as I often found that, when I started to ask
increasingly basic and fundamental questions about neuroimaging
analysis, the students had a very vague idea of the principles, and
were treating the analysis software as a semi-magical box of software
tricks.  This in turn meant that they often couldn't see how to apply
basic statistical reasoning to their analysis.   I also found that
researchers coming to me for advice were making many simple errors in
their analysis scripts, and almost invariably had a disorganized
working process, so they were unable even to work out what they had
done, far less check it for errors.   Over time, my colleagues and I
found ourselves switching to a completely reversed mode of teaching;
instead of teaching ideas, then code, we taught code, then, using
code, taught the ideas - and we rediscovered the wisdom of Richard
Feynman's famous statement - "What I cannot create, I do not understand".   As
we did this, we integrated teaching of organized working practice with code
that we had learned from our work in open-source scientific software.   This
practice dramatically increases the transparency of the analysis, reduces
error, improves collaboration, and leads to reproducibility by design.
I will try to show you how this works, why it is such a powerful way of
explaining, and persuade you that this method was successful in teaching
students of neuroimaging to work more effectively and with greater
understanding.

[^1]: Millman KJ, Brett M, Barnowski R, Poline JB. Teaching Computational
    Reproducibility for Neuroimaging. Front Neurosci. 2018 Oct 22;12:727. doi:
    10.3389/fnins.2018.00727. PMID: 30405329; PMCID: PMC6204391.
